###### Setting

```
# Default django project root
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Generating a SECRET_KEY using the terminal
py manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

