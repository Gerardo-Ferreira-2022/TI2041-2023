from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'home.html')

def calculate(request):
    resultado = None
    mensaje_error = None

    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operador = request.POST.get('operador')

        if operador == 'suma':
            resultado = num1 + num2
        elif operador == 'resta':
            resultado = num1 - num2
        elif operador == 'multiplicacion':
            resultado = num1 * num2
        elif operador == 'division':
            if num2 != 0:
                resultado = num1 / num2
            else:
                mensaje_error = 'División por cero'

        if not operador:
            mensaje_error = 'Debes seleccionar un operador'

    # Redondea el resultado a un número entero
    if resultado is not None:
        resultado = int(resultado)

    return render(request, 'home.html', {'resultado': resultado, 'mensaje_error': mensaje_error})


