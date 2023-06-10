# blog/views.py

from django.shortcuts import render
from django.http import Http404

from blog.models import Post


def post_list(request):

	posts = Post.published.all()

	context = {'posts':posts}
	return render(request, 'blog/post/list.html', context)


def post_detail(request, id):

	try:
		post = Post.published.get(id=id)
	except Post.DoesNotExist:
		raise Http404("No post found.")

	context = {'post':post}
	return render(request, 'blog/post/detail.html', context)
