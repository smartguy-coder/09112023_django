from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_authors.serializers import AuthorSerializer
from books.models import Author


class AuthorsView(APIView):
    def get(self, request):
        limit = int((request.GET.get('limit') or 10))
        skip = int((request.GET.get('skip') or 0))

        authors = Author.objects.all()[skip:skip+limit]
        authors = AuthorSerializer(authors, many=True)
        return Response({'authors': authors.data}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        name = data['name'].title()
        pseudonym = data['pseudonym']
        has_bad_temper = data['has_bad_temper']

        is_author_already_saved = Author.objects.filter(name__iexact=name).exists()
        if is_author_already_saved:
            return Response({'error': 'Author with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)
        author = Author.objects.create(name=name, pseudonym=pseudonym, has_bad_temper=has_bad_temper)
        author = AuthorSerializer(author, many=False)
        return Response({'author': author.data}, status=status.HTTP_201_CREATED)

    def put(self, request):
        data = request.data
        author_id = data['id']
        Author.objects.filter(pk=author_id).update(**data)
        author = Author.objects.get(pk=author_id)
        author = AuthorSerializer(author, many=False)
        return Response({'author': author.data}, status=status.HTTP_200_OK)

    def delete(self, request):
        data = request.data
        author_id = data['id']
        Author.objects.filter(pk=author_id).delete()
        return Response({'status': 'OK'}, status=status.HTTP_200_OK)
