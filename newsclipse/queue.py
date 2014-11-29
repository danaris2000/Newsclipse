import logging

from newsclipse.core import celery as app
from newsclipse.extract import extract_entities

log = logging.getLogger(__name__)


@app.task
def extract(story_id):
    test = "Vladimir Putin is giving Angela Merkel a big fat wet kiss!"
    entities = extract_entities(test)

	
@app.task
def lookup(story_id, entity_name, entity_type):
	pass

	#Here you add code, don't forget
	#that returns a list of different card objects
	switch(n) {
		case "person":
			#run which lookup services
			break;
		case "places":
			#run which lookup services
			break;
		case "social tags":
			#run which lookup services
			break;
		case "companies":
			#run which lookup services
			break;
		case "organisations":
			#run which lookup services
			break;
	}
	
	#title
	#text
	#picture (in case of person)
	#
