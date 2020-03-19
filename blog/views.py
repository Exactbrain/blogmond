from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post, Breaking, Tv, Series
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

#def PostDetail(request, post_id):
#	post = get_object_or_404(Post, pk=post_id)
#	post.body = post.body.replace(" ", "\n")
	#return HttpResponse(var)   this is just what is left, FOR NOW!!!!   

#	posts = Post.objects.order_by('-pub_date')[5:9]
#	all_posts = Post.objects.order_by("-pub_date")[5:]
#	context = {'post': post, 'posts': posts, "all_posts":all_posts}
#	return render(request, 'blog/post_detail.html', context)      AllPostDetail



def AllPost(request):
	posts = Post.objects.order_by('-pub_date')
	context = {'posts': posts}
	return render(request, 'blog/all_post.html', context)

def AllSeries(request):
	series = Series.objects.order_by('-pub_date')
	context = {'series': series}
	return render(request, 'blog/all_series.html', context)
    
def AllTv(request):
	tvs = Tv.objects.order_by('-pub_date')
	context = {'tvs': tvs}
	return render(request, 'blog/all_tv.html', context)
    
    
    
def AllPostDetail(request):
	posts = Post.objects.order_by('-pub_date')
	context = {'posts': posts}
	return render(request, 'blog/index.html', context)
	
def PostDetail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	#post.body = post.body.replace(" ", "\n")
	#return HttpResponse(var)   this is just what is left, FOR NOW!!!!   BreakingDetail

	#posts = Post.objects.order_by('-pub_date')[5:9]
	#all_posts = Post.objects.order_by("-pub_date")[5:]
	context = {'post': post}
	return render(request, 'blog/post_detail.html', context)


def TvDetail(request, tv_id):
	tv = get_object_or_404(Tv, pk=tv_id)
	#post.body = post.body.replace(" ", "\n")
	#return HttpResponse(var)   this is just what is left, FOR NOW!!!!   BreakingDetail

	#posts = Post.objects.order_by('-pub_date')[5:9]
	#all_posts = Post.objects.order_by("-pub_date")[5:]
	context = {'tv': tv}
	return render(request, 'blog/tv_detail.html', context)
		
def SeriesDetail(request, series_id):
	series = get_object_or_404(Series, pk=series_id)
	#post.body = post.body.replace(" ", "\n")
	#return HttpResponse(var)   this is just what is left, FOR NOW!!!!   BreakingDetail

	#posts = Post.objects.order_by('-pub_date')[5:9]
	#all_posts = Post.objects.order_by("-pub_date")[5:]
	context = {'series': series}
	return render(request, 'blog/series_detail.html', context)
	
			
	
def BreakingDetail(request, breaking_id):
	breaking = get_object_or_404(Breaking, pk=breaking_id)
	#post.body = post.body.replace(" ", "\n")
	#return HttpResponse(var)   this is just what is left, FOR NOW!!!!   BreakingDetail

	#posts = Post.objects.order_by('-pub_date')[5:9]
	#all_posts = Post.objects.order_by("-pub_date")[5:]
	context = {'breaking': breaking}
	return render(request, 'blog/breaking_detail.html', context)
		

	
def PostBlog(request):
	if request.method == "POST":
		title = request.POST.get("title")
		pub_date = timezone.now()
		photo = request.FILES["photo"]
		body = request.POST.get("body")
		
		post = Post.objects.create(title=title, body=body, image=photo, pub_date=pub_date)
		post.save()
		return HttpResponseRedirect(reverse("blog:postblog"))
		
	else:
		return render(request, 'blog/post_blog.html')
		
def PostBreaking(request):
	if request.method == "POST":
		title = request.POST.get("title")
		pub_date = timezone.now()
		photo = request.FILES["photo"]
		body = request.POST.get("body")
		
		breaking = Breaking.objects.create(title=title, body=body, image=photo, pub_date=pub_date)
		breaking.save()
		return HttpResponseRedirect(reverse("blog:postbreaking"))
		
	else:
		return render(request, 'blog/post_breaking.html')
		
		
def PostSeries(request):
	if request.method == "POST":
		title = request.POST.get("title")
		pub_date = timezone.now()
		photo = request.FILES["photo"]
		body = request.POST.get("body")
		
		series = Series.objects.create(title=title, body=body, image=photo, pub_date=pub_date)
		series.save()
		return HttpResponseRedirect(reverse("blog:postseries"))
		
	else:
		return render(request, 'blog/post_series.html')
		
		
def PostTv(request):
	if request.method == "POST":
		title = request.POST.get("title")
		pub_date = timezone.now()
		video = request.FILES["photo"]
		body = request.POST.get("body")
		
		tv = Tv.objects.create(title=title, body=body, video=video, pub_date=pub_date)
		tv.save()
		return HttpResponseRedirect(reverse("blog:posttv"))
		
	else:
		return render(request, 'blog/post_tv.html')
		

def index(request):
    if request.method == 'GET' and request.GET.get('query') != None:
        query = request.GET.get('query')
        posts = Post.objects.filter(
            title__icontains=query)
        #quotes = Quotes.objects.order_by('-pk')[:1]

        #for quote in quotes:
        #    quote = get_object_or_404(Quotes, pk=quote.id)
        return render(request, 'blog/index.html', {'posts': posts})

    else:
    	breaking = Breaking.objects.order_by('-pub_date')[0]
    	tv = Tv.objects.order_by('-pub_date')[:5]
    	series = Series.objects.order_by('-pub_date')[:5]
    	posts = Post.objects.order_by('-pub_date')[:5]
    	all_posts = Post.objects.order_by("-pub_date")[:12]
    	context = {'posts': posts, "all_posts":all_posts, "breaking":breaking, "tv":tv, "series":series}
    	return render(request, 'blog/index.html', context)



