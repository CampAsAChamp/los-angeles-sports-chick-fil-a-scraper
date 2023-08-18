import os

import util

FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')  # Comma separate list of emails
PASSWORD = os.getenv('PASSWORD')
SHOULD_SEND_EMAIL = util.readBoolEnvVar('SHOULD_SEND_EMAIL', 'True')
USE_LOCAL = util.readBoolEnvVar('USE_LOCAL', 'False')
