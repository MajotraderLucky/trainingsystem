from rest_framework.decorators import api_view
from rest_framework.response import Response
from trainingsystem.models import Lesson, UserLesson

@api_view(['GET'])
def lessons_list(request):
  user = request.user # getting the current user
  # get lessons related to products that the user has access to
  lessons = Lesson.objects.filter(product_in=user.productaccess_set.values_list('product, flat=True'))
  lessons_data = []
  for lesson in lessons:
    # get information about the user viewing the lesson
    user_lesson = UserLesson.objects.get(user=user, lesson=lesson)
    status = user_lesson.status
    watched_time = user_lesson.watched_time

    lessons_data = {
      'title': lesson.title,
      'video_link': lesson.video_link,
      'duration': lesson.duration,
      'status': status,
      'watched_time': watched_time
    }
    lessons_data.append(lessons_data)

  return Response(lessons_data)