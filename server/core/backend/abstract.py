from allauth.socialaccount.models import SocialToken

'''
Abstract client mixin class
Used to implements API client (with dedicated lib)
A "provider_name" prop has to be defined for each child class
'''
class AbstractClient():
  
    def get_social_token(self, user): 
        try:
            token = SocialToken.objects.get(
                account__user=user, 
                account__provider=self.provider_name
            )
            return token
        except SocialToken.DoesNotExist:
            return None

    # Method needs to be implemented in child class
    def get_client(self, user):
        pass

    # Refresh stored django allauth token
    def update_refresh_token(self, user, new_token, new_refresh_token, new_expires_at): 
        token = self.get_social_token(user)
        token.access_token = new_token
        token.token_secret = new_refresh_token
        token.expires_at = new_expires_at
        token.save()
        return token
