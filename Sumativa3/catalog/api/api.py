from ninja import NinjaAPI, Swagger, Redoc
from services.models import Provider, Service, Address, Contact
from django.http import JsonResponse
from ninja import Schema
from datetime import datetime

api = NinjaAPI(docs=Redoc())

def service_tojson(Service):
    data = {
        'id':Service.id,
        'name': Service.name,
        'description': Service.description,
        'provider': {
            'fantasy_name': Service.provider.fantasy_name,
            'tax_name': Service.provider.tax_name,
            'tax_id': Service.provider.tax_id,
            'enabled': Service.provider.enabled,
        },
        'price': Service.price,
        'from_date': Service.from_date,
        'thru_date': Service.thru_date
    }

    return data

@api.get("/service")
def get_service(request):
    services = Service.objects.all()
    data = []
    for service in services:
        data.append(service_tojson(service))
    return data


@api.get("/service/{id}")
def get_service_id(request, id):
    service = Service.objects.get(id=id)
   
    return service_tojson(service)



class ServiceInputSchema(Schema):
    name: str
    description: str
    provider: int
    price: float
    from_date: str
    thru_date: str

class ServiceOutputSchema(Schema):
    id: int
    name: str
    description: str
    provider: int
    price: float
    from_date: str
    thru_date: str

@api.post("/service", response={200: ServiceOutputSchema}, summary="Create a new service")
def post_service(request, service: ServiceInputSchema):
    
    try:
        provider = Provider.objects.get(id=service.provider)
    except:
        return {"error": "Provider not found"}

    new_service = Service.objects.create(
        name=service.name,
        description=service.description,
        provider=provider,
        price=service.price,
        from_date=service.from_date,
        thru_date=service.thru_date
    )

    new_service.save()

    
    return service_tojson(new_service)

@api.delete("/service/{id}", response={200: ServiceOutputSchema}, summary="Eliminar servicio agregando fecha de termino")
def delete_service(request, id: int):
    try:
        service = Service.objects.get(id=id, thru_date__isnull=True)
    except Service.DoesNotExist:
        return JsonResponse({'error': 'Error al eliminar'}, status=404)

    # Set the thru_date to the current date
    service.thru_date = datetime.now()
    service.save()

    return service_tojson(service)