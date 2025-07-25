from django.core.management.base import BaseCommand
from django.conf import settings
import helpers


STATICFILES_VENDOR_DIR = getattr(settings,'STATICFILES_VENDOR_DIR')

VENDOR_STATICFILES = {
      
      "flowbite.min.css":"https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
      "flowbite.min.js":"https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js"
}

class Command(BaseCommand):

    def handle(self, *args, **options):
           self.stdout.write("Downloading vendor static files...")
           completed_urls = []
           for name , url in VENDOR_STATICFILES.items():
               self.stdout.write(f"Downloading {name} from {url}")
               destination = STATICFILES_VENDOR_DIR / name
               dl_success = helpers.download_to_local(url,destination)
               if dl_success:
                     completed_urls.append(url)
               else:
                    self.stdout.write(
                         self.style.ERROR(f"Failed to download {url}")
                    )
           if set(completed_urls) == set(VENDOR_STATICFILES.values()):
                self.stdout.write(self.style.SUCCESS("Vendor staticfiles downloaded successfully."))
           else:
                self.stdout.write(self.style.WARNING("Some vendor static files failed to download."))
                    
                               
            
               