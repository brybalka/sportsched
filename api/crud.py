from datetime import date, datetime
from model import UFCEventModel, Session
from typing import List
from typing import Union, List


def get_ufc_events(start_date: Union[date, None], fighters: Union[List[str], None], limit: Union[int, None]) -> List[
    UFCEventModel]:
    session = Session()
    qry = session.query(UFCEventModel)
    if start_date != None:
        qry = qry.filter(UFCEventModel.date >= start_date)
    else:
        qry = qry.filter(UFCEventModel.date > datetime.now())

    if limit != None:
        qry = qry.limit(limit)
    else:
        qry = qry.limit(100)

    ufc_events = qry.all()
    session.close()

    return ufc_events
