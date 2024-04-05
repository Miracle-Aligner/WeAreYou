from datetime import datetime

screening_md_template = '''
<div class="screening-preview">
    <div class="line-one highlight-blue">{}</div>
    <br>
    <div class="line-two highlight-blue">USA</div>
    <br>
    <div class="screening-date highlight">12 April 2024, 3 PM</div>
    <a class="btn btn-primary display_bold d-none" href="#register">Register</a>
</div>
<div class="overlay-content position-absolute bottom-0 start-0 w-100">
    <div class="overlay-inner">
        <h3>New York</h3>
        <div class="">
            <p class="overlay-details">12TH April, 3 РМ <br>
                82 Columbus Ave, Thornwood, NY 10594 <br>
                New York, USA 
                </p>
            <a class="btn btn-primary display_bold d-none" href="">Register</a>
        </div>
    </div>
</div>'''

screenings_mobile_template = '''
<div class="swiper-slide">
    <div class="screening-card">
        <div class="screening-preview">
            <div class="card-color-top" style="background-image: url({{ url_for('static', filename='images/{image_name}') }});"></div>
            <div class="card-body">
                <h5 class="card-title">{event_host_institution}</h5>
                <p class="card-text">{country}<br>{date_time}<br>
            </div>

            <div class="overlay-content position-absolute bottom-0 start-0 w-100">
                <div class="overlay-inner">
                    <h3>{event_host_institution}</h3>
                    <div class="">
                        <p class="overlay-details">
                            {date_time}<br>
                            {full_address}
                        </p>
                        <a class="btn btn-primary display_bold{registration_class}" href="{registration_link}">{register_button_text}</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

'''

def get_md_screenings_html(events_list):
    return split_into_six(events_list)


def split_into_six(input_list):
    # The size of each chunk
    chunk_size = 6

    # Splitting the input list into chunks of size six
    chunks = [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

    blank = {
            'register_button_text': '',
             'image_name': 's_blank.png',
             'event_host_institution': '',
             'country': '',
             'registration_link': '',
             'registration_open': False,
             'date': '',
             'time': '',
             'full_address': '',
             'date_time': '',
             'registration_class': ' d-none'
             }
    # Check if the last chunk needs padding
    if chunks and len(chunks[-1]) < chunk_size:
        # Calculate how many blank values are needed
        blanks_needed = chunk_size - len(chunks[-1])

        # Pad the last chunk with blank values
        chunks[-1].extend([blank for _ in range(blanks_needed)])

    return chunks

def sort_events_by_date(events):
    # Convert date strings to datetime objects for comparison
    for event in events:
        event['date'] = datetime.strptime(event['date'], '%Y-%m-%d')

    # Get today's date for comparison
    today = datetime.now().date()

    # Separate upcoming and past events
    upcoming_events = [event for event in events if event['date'].date() >= today]
    past_events = [event for event in events if event['date'].date() < today]

    # Sort both lists in ascending order of dates
    upcoming_events.sort(key=lambda event: event['date'])
    past_events.sort(key=lambda event: event['date'])

    # Concatenate the sorted lists, with upcoming_events first
    sorted_events = upcoming_events + past_events

    # Convert datetime objects back to string for output
    for event in sorted_events:
        event['date'] = event['date'].strftime('%d.%m')
        date_time = "{date}, {time}".format(date=event['date'], time=event['time']) if event['time'] else event[
            'date']
        event['date_time'] = date_time
        registration_class = " d-none" if not event['registration_open'] else ''
        event['registration_class'] = registration_class

    return sorted_events