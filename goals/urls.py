from django.urls import path

from .views import (HomePageView,
                    GoalsView, 
                    GoalDetailView, 
                    GoalCreateView, 
                    GoalUpdateView,
                    GoalDeleteView)


urlpatterns = [ 
    path('', HomePageView.as_view(), name='home'),
    path('goals/', GoalsView.as_view(), name='goals_list'),
    path('goal/<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
    path('goal/new/', GoalCreateView.as_view(), name='goal_create'),
    path('goal/edit/<int:pk>/', GoalUpdateView.as_view(), name='goal_update'),
    path('goal/delete/<int:pk>/', GoalDeleteView.as_view(), name='goal_delete'),
]
