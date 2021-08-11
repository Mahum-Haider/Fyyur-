#  Create Venue
#  ----------------------------------------------------------------
@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
  form = VenueForm(request.form)
  if form.validate():  
    try:
      venue = Venue(
        name = request.form['name'],
        address = request.form['address'],
        city = request.form['city'],
        state = request.form['state'],
        phone = request.form['phone'],
        website = request.form['website'],
        facebook_link = request.form['facebook_link'],
        image_link = request.form['image_link'],
        genres = request.form['genres'],
        seeking_description = request.form['seeking_description'],
        seeking_talent = True if 'seeking_talent' in request.form else False
      )

      db.session.add(venue)
      db.session.commit()
    

  # on successful db insert, flash success
  # flash('Venue ' + request.form['name'] + ' was successfully listed!')

    except():
      db.session.rollback()
      error = True
      print(sys.exc_info())
    finally:
      db.session.close()
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    if error:
      flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
    else:
      flash('No errors. Venue ' + request.form['name'] + ' are listed.')

  return render_template('pages/home.html')
