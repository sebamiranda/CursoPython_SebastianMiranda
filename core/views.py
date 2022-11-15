import json
from django.core.serializers import serialize
from datetime import datetime
from django.http import HttpResponse
from rest_framework.status import *
from rest_framework.views import APIView
from core.models import *


# Create your views here.


class BookView(APIView):
    def get(self, request, author_name=None):
        if author_name:
            if Author.objects.filter(first_name__icontains=author_name).exists():
                book_response = list(Book.objects.filter(author__first_name__icontains=author_name))
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Author not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            book_response = Book.objects.all()
        book_response = serialize('json', book_response)
        return HttpResponse(content_type='application/json',
                            content=book_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['author'] = Author.objects.get(pk=body['author'])
        body['category'] = Category.objects.get(pk=body['category'])
        book, created = Book.objects.get_or_create(**body)
        if created:
            book.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book created successfully'}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not exist'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        book.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book update successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Book not found'}),
                                status=HTTP_404_NOT_FOUND)
        book.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Book deleted successfully'}),
                            status=HTTP_200_OK)


class CategoryView(APIView):
    def get(self, request, category_name=None):
        if category_name:
            if Category.objects.filter(category_name__icontains=category_name).exists():
                category_response = Category.objects.filter(category_name__icontains=category_name)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Category not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            category_response = Category.objects.all()
        category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=category_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        category, created = Category.objects.get_or_create(**body)
        if created:
            category.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category already exist'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        category.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Category not found'}),
                                status=HTTP_404_NOT_FOUND)
        category.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Category deleted successfully'}),
                            status=HTTP_200_OK)


class AuthorView(APIView):
    def get(self, request, last_name=None):
        if last_name:
            if Author.objects.filter(last_name__icontains=last_name).exists():
                author_response = Author.objects.filter(last_name__icontains=last_name)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Author not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            author_response = Author.objects.all()
        author_response = serialize('json', author_response)
        return HttpResponse(content_type='application/json',
                            content=author_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        author, created = Author.objects.get_or_create(**body)
        if created:
            author.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author already exist'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        author.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author not found'}),
                                status=HTTP_404_NOT_FOUND)
        author.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author deleted successfully'}),
                            status=HTTP_200_OK)


class PartnerView(APIView):
    def get(self, request, dni=None):
        if dni:
            if Partner.objects.filter(dni__icontains=dni).exists():
                partner_response = Partner.objects.filter(dni__icontains=dni)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Partner not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            partner_response = Partner.objects.all()
        partner_response = serialize('json', partner_response)
        return HttpResponse(content_type='application/json',
                            content=partner_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        partner, created = Partner.objects.get_or_create(**body)
        if created:
            partner.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner created successfully',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner already exist'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        partner.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Partner not found'}),
                                status=HTTP_404_NOT_FOUND)
        partner.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Partner deleted successfully'}),
                            status=HTTP_200_OK)


class BookLoan(APIView):
    def get(self, request, dni=None):
        if dni:
            if BookLoan.objects.filter(partner__dni=dni).exists():
                bookloan_response = BookLoan.objects.filter(partner__dni=dni)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'BookLoan not found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            bookloan_response = BookLoan.objects.all()
        bookloan_response = serialize('json', bookloan_response)
        return HttpResponse(content_type='application/json',
                            content=bookloan_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['book'] = Book.objects.get(pk=body['book'])
        body['partner'] = Partner.objects.get(pk=body['partner'])
        bookloan, created = BookLoan.objects.get_or_create(**body)
        if created:
            bookloan.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'BookLoan created successfully'}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'BookLoan already exists'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, bookloan_id):
        bookloan = BookLoan.objects.filter(pk=bookloan_id)
        if not bookloan.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'BookLoan not found'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['date_devolucion'] = datetime.now()
        bookloan.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Bookloan updated successfully'}),
                            status=HTTP_200_OK)

    def delete(self, request, bookloan_id):
        bookloan = BookLoan.objects.filter(pk=bookloan_id)
        if not bookloan.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'BookLoan not found'}),
                                status=HTTP_404_NOT_FOUND)
        bookloan.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'BookLoan deleted successfully'}),
                            status=HTTP_200_OK)
