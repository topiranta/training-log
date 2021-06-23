from app import app

def errormessage(error):

	errormessage = ''

	if error == 'login_failed':

		errormessage = 'Kirjautuminen epäonnistui: käyttäjä tai salasana on väärä'

	elif error == 'unmatching_passwords':

		errormessage = 'Syöttämäsi salasanat eivät täsmää'

	elif error == 'password_length':

		errormessage = 'Salasanan tulee olla vähintään neljä ja korkeintaan 32 merkkiä pitkä'

	elif error == 'username_not_available':

		errormessage = 'Käyttäjätunnus ei ole vapaana'

	elif error == 'username_not_valid':

		errormessage = 'Käyttäjätunnuksen pituuden tulee olla vähintään 1 merkki ja korkeintaan 16 merkkiä'

	elif error == 'exercise_not_valid':

		errormessage = 'Syöttämäsi harjoitus ei kelpaa. Tarkista, että kaikissa kentissä on arvot, harjoituksen kuvaus on korkeintaan 20 merkkiä, pituus korkeintaan 1000 km, kesto korkeintaan 3000 min ja syke välillä 40-250'

	elif error == 'comment_not_valid':

		errormessage = 'Kommentin tulee olla vähintään 1 merkki ja korkeintaan 64 merkkiä'

	return errormessage