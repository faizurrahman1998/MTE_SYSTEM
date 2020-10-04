import os
from django.conf import settings

class Helper_Functions: 

    @staticmethod
    def delete_image(request): 

        if request.user.is_authenticated:
            
            name = "".join(list((request.user.first_name).split(" ")))

            for root, _, files in os.walk(settings.MEDIA_ROOT): 
                for img in files: 
                    
                    if img.rsplit(".", 1)[0] == name: 
                        os.remove(os.path.join(root, img))

                        return True
        
        return False