import random
import sqlite3

	
def contingency_response(text):
	conn = sqlite3.connect('app/contingency/store.db')
	print "Opened database, querying..."
	cursor = conn.execute("SELECT ID, response, tags, ranking FROM Defaults ORDER BY ranking")

	allresp = []
	alltags = []
	for row in cursor:
		allresp.append(row[1])
		alltags.append(row[2].lower())

	l = len(allresp)

	print "Processing hypothesis: \'" + text + "\'"
	resp = ""

	extracted_tags = text.split(' ')
	matches_max = 0
	matched = False

	for i in range(0, l):
		tags = alltags[i].lower()
		matches = 0
		for etag in extracted_tags:
			if etag in tags:
				matches += 1
				matched = True
		if matches > matches_max:
			matches_max = matches
			resp = allresp[i]

	if not matched:
		resp = allresp[random.randint(0, l-1)]

	if len(resp) == 0:
		resp = "Internal processing error"

	wmatched = float(matches_max)/float(len(extracted_tags))

	conn.close()
	return resp, extracted_tags, wmatched