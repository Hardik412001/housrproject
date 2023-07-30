# from django.http import JsonResponse
# from loginsys.models import CommunityEvent


# def import_residents(request):
#     # return redirect('login')
#     # if request.method == 'POST':
#     if True:

#         try:
#             data = {
#   "community_events": [
#     {
#       "name": "Charity Walkathon",
#       "date": "2023-08-15",
#       "description": "Join us for a charity walkathon to support local causes."
#     },
#     {
#       "name": "Community Cleanup Drive",
#       "date": "2023-09-10",
#       "description": "Help keep our community clean by participating in this cleanup drive."
#     },
#     {
#       "name": "Cultural Festival",
#       "date": "2023-10-25",
#       "description": "Experience the diverse cultures of our community through music, dance, and food."
#     },
#     {
#       "name": "Health and Fitness Workshop",
#       "date": "2023-11-05",
#       "description": "Learn about staying fit and healthy with experts in this workshop."
#     },
#     {
#       "name": "Food Drive",
#       "date": "2023-12-20",
#       "description": "Contribute to the food drive and help provide meals to those in need."
#     },
#     {
#       "name": "Environmental Awareness Seminar",
#       "date": "2024-01-15",
#       "description": "Raise awareness about environmental issues and sustainable practices."
#     },
#     {
#       "name": "Community Sports Day",
#       "date": "2024-02-12",
#       "description": "Participate in various sports activities and enjoy a fun-filled day with the community."
#     },
#     {
#       "name": "Art and Craft Exhibition",
#       "date": "2024-03-20",
#       "description": "Showcase your creativity or appreciate the art and craft talents of our community members."
#     },
#     {
#       "name": "Educational Fair",
#       "date": "2024-04-10",
#       "description": "Explore educational opportunities and resources available in our community."
#     },
#     {
#       "name": "Music Concert",
#       "date": "2024-05-05",
#       "description": "Enjoy an evening of musical performances by local talents in our community."
#     }
#   ]
# }



#             events_data = data.get('community_events', [])
#             for event_data in events_data:
#                 CommunityEvent.objects.create(
#                     name=event_data.get('name'),
#                     date=event_data.get('date'),
#                     description=event_data.get('description'),
#                 )
#             print('message Data imported successfully.')
#             return HttpResponse("message Data imported successfully.")
#         except Exception as e:
#             traceback.print_exc()
