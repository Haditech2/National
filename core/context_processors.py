from datetime import datetime, date


def election_countdown(request):
    """Context processor to provide election countdown data globally."""
    current_year = datetime.now().year
    election_date = date(current_year, 12, 26)
    
    today = date.today()
    
    if election_date < today:
        # If election date has passed this year, use next year
        election_date = date(current_year + 1, 12, 26)
    
    days_remaining = (election_date - today).days
    
    return {
        'election_date': election_date,
        'days_to_election': days_remaining,
        'election_year': election_date.year,
    }
