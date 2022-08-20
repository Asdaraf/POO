from release import Report, HTMLReport, ConsoleReport, read_content, ParagraphReport
import builtins
import contextlib, io
from unittest.mock import Mock

def test_function(method, expected_value, arg=None):
    #https://stackoverflow.com/questions/62360192/how-to-check-that-print-was-called-in-a-function
    mock = Mock()
    mock.side_effect = print  # ensure actual print is called to capture its txt
    print_original = print
    builtins.print = mock
    print(f'El método Ejecutado fue: {method.__name__}')
    try:
        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            if arg:
                method(arg)
            else:
                method()
        output = str_io.getvalue()

        assert print.called  # `called` is a Mock attribute
        print(f'valor experado del output de tu funcion:\n {expected_value}')
        print(f' Valor que retorno tu funcion: \n {output}')
        assert output.startswith(expected_value)
        print('Parece que todo ocurrio bien \n')
        
    finally:
        builtins.print = print_original  # ensure print is "unmocked"

if __name__ == '__main__':
    print('Hola, bienvenide al main.py \n acá poderas testear su código')
    print('Para testear la clase Report digite 0')
    print('Para testear la clase HTMLReport digite 1')
    print('Para testear la clase ParagraphReport digite 2')
    print('Para testear la clase consoleReport digite 3')
    print('Para salir digite 4')
    respuesta = input()
    if respuesta == '0':
        try:
            contenido = (read_content('content.csv'))
            report = Report('Report', 'Test Report', 100, 10, contenido)
            test_function(report.output_body,
             '1-')
        except FileNotFoundError as err:
            print(err)
            print('\nPorfavor verifica si el archivo main.py está en la misma carpeta que content.csv')

        except TypeError as err:
            print (err)
            print('\nHiciste algo mal al hacer el constructor(__init__) verifica si esta bien el número de atributos')

        except SyntaxError as err:
            print(err)
            print('\n Tiene un Error de Syntaxis, escribiste algo mal, te recomiendo copiar el error de arriba y buscarlo en google que te va salir como resolverlo o tambien puede nos escribir =D')

        except AssertionError as err:
            print(err)
            print('\n Parece que no estás leyendo correctamente =(, recuerda si estas muy perdide puedes mandar un correo y contestamos feliz =)')

    if respuesta == '1':
        try:
            contenido = (read_content('content.csv'))
            html_report1 = HTMLReport('Consulta 1', 'Consulta 1', 100, 80, contenido)

        except FileNotFoundError as err:
            print(err)
            print('\nPorfavor verifica si el archivo main.py está en la misma carpeta que content.csv')

        except TypeError as err:
            print (err)
            print('\nHiciste algo mal al hacer el constructor(__init__) verifica si esta bien el número de atributos o si hiciste correctamente la herencia')
        
        try:
            test_function( html_report1.output_start, '<html>')
            test_function( html_report1.output_head, '<head>')
            test_function( html_report1.output_body_start, '<body>')
            html_report1.output_line('hola soy una linea de teste')
            test_function( html_report1.output_body_end, '</body>')
            test_function( html_report1.output_end, '</html>')
            print('\nParece que no hay ningun error(eso no asegura que este bien, pero muy probable que si)')
        except AssertionError as err:
            print(err)
            print('\n Hola, ese Error es porque lo que imprimiste en el método arriba está mal, puede ser por un espacio, coma o todo el output')

    if respuesta == '2':
        try:
            contenido = (read_content('content.csv'))
            paragraph_report = ParagraphReport(name='ParagraphReport', tittle='Un titulo cualquiera', sample_size=100, maxlength=26, content=contenido, align='right')

        except FileNotFoundError as err:
            print(err)
            print('\nPorfavor verifica si el archivo main.py está en la misma carpeta que content.csv')

        except TypeError as err:
            print (err)
            print('\nHiciste algo mal al hacer el constructor(__init__) verifica si esta bien el número de atributos o si hiciste correctamente la herencia')
        
        try:
            
            test_function( paragraph_report.output_head, '   Un titulo cualquiera')

            test_function(paragraph_report.output_line,
             expected_value='    soy una linea de teste',
              arg='soy una linea de teste')

            print('\nParece que no hay ningun error(eso no asegura que este bien, pero muy probable que si)')
        except AssertionError as err:
            print(err)
            print('\n Hola, ese Error es porque lo que imprimiste en el método arriba está mal,\n puede ser por un espacio o porque no seguiste la metrica del align correctamente, o puede ser que todo el output este mal tambien \n ** IMPORTANTE ese codigo solo verifica si esta bien el alinamiento, puede que te aparezca esse error y aun tenga el iten 100% bueno**')

    if respuesta == '3':
        try:
            contenido = (read_content('content.csv'))
            console_report = ConsoleReport('ConsoladeTestes', 'SuperConsola', 70, 60, contenido)

        except FileNotFoundError as err:
            print(err)
            print('\nPorfavor verifica si el archivo main.py está en la misma carpeta que content.csv')

        except TypeError as err:
            print (err)
            print('\nHiciste algo mal al hacer el constructor(__init__) verifica si esta bien el número de atributos o si hiciste correctamente la herencia')
        
        
        else:
            print('Para la consola no se testea los metodos de forma individual')
            console_report.output_report()
