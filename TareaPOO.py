
class Report():

    def __init__(self, name, tittle, sample_size, maxlenght, content):
        ## Se Renombra variables para comodidad del trabajo
        self.nombre = name
        self.titulo = tittle
        self.tamaño_de_muestra = sample_size
        self.largo_maximo = maxlenght
        self.contenido = content

    def output_report(self):
        # NO MODIFICAR
        self.output_start()
        self.output_head()
        self.output_body_start()
        self.output_body()
        self.output_body_end()
        self.output_end()

    def output_body(self):
                
        self.contenido = self.contenido[5:] ## Se comienza a leer el contenido desde el reporte
        j = 0
        ## Iterar el contenido restringiendo el sample_size y midiendo el largo solicitado
        for linea in self.contenido:
            if j < self.tamaño_de_muestra:
                if len(linea) > self.largo_maximo:
                    div = (len(linea)//self.largo_maximo)
                    for i in range(1,div+2):
                        if j < self.tamaño_de_muestra:
                            linea2 = linea[self.largo_maximo*(i-1):self.largo_maximo*i]
                            self.output_line(linea2)
                        else:
                            break
                        j += 1
                elif len(linea) <= self.largo_maximo:
                    if j < self.tamaño_de_muestra:
                        self.output_line(linea)
                        j += 1
            else:
                break        
                
    def output_start(self):
        pass
   
    def output_head(self):
        pass

    def output_body_start(self):
        pass

    def output_line(self, line):
        print(line)

    def output_body_end(self):
        pass

    def output_end(self):
        pass


# COMPLETAR
class HTMLReport(Report):
    
    def __init__(self, name, tittle, sample_size, maxlenght, content):
        super().__init__(name, tittle, sample_size, maxlenght, content)
        
    def output_start(self):
        print("<html>")

    def output_head(self):
        # NO MODIFICAR
        print('  <head>')
        print(f'    <tittle> {self.titulo} </tittle>')
        print('  </head>')
    
    def output_body_start(self):
        print("  <body>")

    def output_line(self, line):
        print(f"    <p> {line} </p>")

    def output_body_end(self):
        print("  </body>")

    def output_end(self):
        print("</html>")

# COMPLETAR
class ParagraphReport(Report):
    
    def __init__(self, name, tittle, sample_size, maxlenght, content, align):
        super().__init__(name, tittle, sample_size, maxlenght, content)
        self.alinear = align

    def output_start(self):
        pass

    def output_head(self):
        # NO MODIFICAR
        print(f"{self.titulo:^{self.largo_maximo}}")

    def output_body_start(self):
        pass

    def output_line(self, line):
        maxlength = 10
        # NO MODIFICAR
        if self.alinear == "left":
            print(f"{line:<{self.largo_maximo}}")
        elif self.alinear == "right":
            print(f"{line:>{self.largo_maximo}}")
        else:
            print(f"{line:^{self.largo_maximo}}")
        
    def output_body_end(self):
        pass

    def output_end(self):
        pass

# COMPLETAR            
class ConsoleReport(Report):
    
    def __init__(self, name, tittle, sample_size, maxlenght, content, align):
        super().__init__(name, tittle, sample_size, maxlenght, content)
        self.alinear = align
    pass

    def output_start(self):
        print("Bienvenide al generador de reporte en consola")

    def output_head(self):
        print("--*--*--*-- Console Report --*--*--*--")

    def output_body_start(self):
        print("Acá comienza el cuerpo del reporte")

    def output_body(self):
        ## Condiciones e input para ingresar la consulta
        for linea in self.contenido:
            if not "*" in linea:
                self.output_line(linea)
            elif "*" in linea:
                consulta = int(input("Pofavor Digite el número correspondente a su opción (1,2 o 3): "))
                if consulta == 1:
                    html_report = HTMLReport("HTML Report", "Consulta 1", 100, 60, contenido)
                    html_report.output_report()
                    break
                elif consulta == 2:
                    paragraph_report = ParagraphReport("Paragraph Report", "Consulta 2", 100, 60, contenido, "center")
                    paragraph_report.output_report()
                    break
                elif consulta == 3:
                    exit()
        
    def output_line(self, lines):
        print(lines)

    def output_body_end(self):
        print("Acá finaliza el cuerpo del reporte")

    def output_end(self):
        print("¡Gracias por generar un reporte en consola, vuelva pronto!")

def read_content(path):
    with open(path, 'r', encoding='utf-8') as file:
        file_lines = []
        for line in file:
            file_lines.append(line.strip())
    return file_lines

if __name__ == '__main__':
    contenido = (read_content('content.csv'))
    # print(contenido)

console_report = ConsoleReport("Report", "Console Report", 10, 60, contenido, "center")
console_report.output_report()