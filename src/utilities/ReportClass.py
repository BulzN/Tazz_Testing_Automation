# ReportClass.py - Modul .py care îl folosesc pentru a salva un fișier de tip .log pentru a vedea fiecare pas executat
# la nivelul fiecărui test ( Un fel de registru, ca să îl denumesc așa )

import logging
import pytest
import inspect


@pytest.mark.usefixtures("setup")
class ReportClass:
    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        return logger

# EOF
