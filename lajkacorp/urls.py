from django.urls import path
from lajkacorp import views


urlpatterns = [


    path('artist_list/', views.ArtistAlbumsListView.as_view(), name='artist_list'),
    path('add_artist/', views.AddArtistView.as_view(), name='add_artist'),
    path('income_all', views.IncomeListViewAll.as_view(), name='income_all'),
    path('update_artist/<int:pk>/', views.ArtistUpdateView.as_view(), name='update_artist'),
    path('delete_artist/<int:pk>/', views.ArtistDeleteView.as_view(), name='delete_artist'),
    path('add_album/', views.AddAlbumView.as_view(), name='add_album'),
    path('delete_album/<int:pk_album>/', views.DeleteAlbumView.as_view(), name='delete_album'),
    path('add_income/', views.AddIncomeView.as_view(), name='add_income'),
    path('income_list/', views.IncomeListView.as_view(), name='income_list'),
    path('income_list/update_income/<int:pk>/', views.IncomeUpdateView.as_view(), name='update_income'),
    path('income_list/delete_income/<int:pk>/', views.IncomeDeleteView.as_view(), name='delete_income'),
    path('add_storeroom/', views.AddStoreRoomView.as_view(), name='add_storeroom'),
    path('storeroom/', views.StoreRoomView.as_view(), name='storeroom'),
    path('storeroom_user/', views.StoreroomUserView.as_view(), name='storeroom_user'),
    path('update_storeroom/<int:pk>/', views.UpdateStoreRoomView.as_view(), name='update_storeroom'),
    path('delete_storeroom/<int:pk>/', views.DeleteStoreRoomView.as_view(), name='delete_storeroom'),
    path('add_distro_chanel/', views.AddDistroView.as_view(), name='add_distro'),
    # path('message/', views.MessageDetailView.as_view(), name='message'),
    path('settings/income_spliter/', views.AddIncomeSpliter.as_view(), name='add_inc_split'),


]