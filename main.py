# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


#add_time("11:15 PM", "00:45")


# Run unit tests automatically
main(module='test_module', exit=False)

