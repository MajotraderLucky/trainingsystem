from rest_framework.decorators import api_view
from rest_framework.response import Response
from trainingsystem.models import Lesson, UserLesson

@api_view(['GET'])
def lessons_list(request):
  user = request.user # getting the current user
  product_id = request.GET.get('product_id')
  # get lessons related to products that the user has access to
  lessons = Lesson.objects.filter(product_id=product_id, product_productacces__user=user)
  lessons_data = []
  for lesson in lessons:
    # get information about the user viewing the lesson
    user_lesson = UserLesson.objects.get(user=user, lesson=lesson)
    status = user_lesson.status
    watched_time = user_lesson.watched_time
    last_watched_date = user_lesson.last_watched_date

    lessons_data = {
      'title': lesson.title,
      'video_link': lesson.video_link,
      'duration': lesson.duration,
      'status': status,
      'watched_time': watched_time,
      'last_watched_date': last_watched_date
    }
    lessons_data.append(lessons_data)

  return Response(lessons_data)