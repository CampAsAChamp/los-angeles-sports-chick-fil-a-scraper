import os

import helpers

FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')  # Comma separate list of emails
PASSWORD = os.getenv('PASSWORD')
SHOULD_SEND_EMAIL = helpers.readBoolEnvVar('SHOULD_SEND_EMAIL', 'True')
USE_LOCAL = helpers.readBoolEnvVar('USE_LOCAL', 'False')
