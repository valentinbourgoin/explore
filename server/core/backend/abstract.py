from allauth.socialaccount.models import SocialToken

'''
Abstract client mixin class
Used to implements API client (with dedicated lib)
A "provider_name" prop has to be defined for each child class
'''
class AbstractClient():

    def __init__(self, user):
        self.user = user
        self.client = self.get_client()
  
    def get_social_token(self): 
        try:
            token = SocialToken.objects.get(
                account__user=self.user, 
                account__provider=self.provider_name
            )
            return token
        except SocialToken.DoesNotExist:
            return None

    # Method needs to be implemented in child class
    def get_client(self):
        pass

    # Refresh stored django allauth token
    def update_refresh_token(self, new_token, new_refresh_token, new_expires_at): 
        token = self.get_social_token()
        token.access_token = new_token
        token.token_secret = new_refresh_token
        token.expires_at = new_expires_at
        token.save()
        return token
