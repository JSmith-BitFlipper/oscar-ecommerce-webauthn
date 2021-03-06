from django.contrib.auth.decorators import login_required
from django.urls import path

import oscar.apps.customer.apps as apps

class CustomerConfig(apps.CustomerConfig):
    name = 'customer'

    def get_urls(self):
        # Get the original `urls`
        urls = super().get_urls()

        # List the `new_urls` and post_process them
        new_urls = [
            path('login_begin/', self.login_view.as_view(), name='login_begin'),
            path('login_finish/', self.login_view.as_view(), name='login_finish'),

            path('register_begin/', self.login_view.as_view(), name='register_begin'),
            path('register_finish/', self.login_view.as_view(), name='register_finish'),

            path('profile/delete_begin/', login_required(self.profile_delete_view.as_view()), name='delete_profile_begin'),
            path('profile/delete_finish/', login_required(self.profile_delete_view.as_view()), name='delete_profile_finish'),
        ]

        new_urls = self.post_process_urls(new_urls)

        # Return all of the urls
        return urls + new_urls
