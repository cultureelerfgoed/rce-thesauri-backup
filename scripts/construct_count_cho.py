import datetime
import requests
import argparse

# Argument parsing for dynamic filename
parser = argparse.ArgumentParser(description='Run SPARQL query and save the result.')
parser.add_argument('--output', type=str, help='The output file path', required=True)
args = parser.parse_args()

# Stap 1: Haal de huidige datum en tijd op om de graph naam te genereren
current_time = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
new_graph_uri = f"https://linkeddata.cultureelerfgoed.nl/graph/instanties-rce/count{current_time}"

# Stap 2: Voer de SPARQL CONSTRUCT query uit via de gegeven API URI met paginering
page = 1
page_size = 200
sparql_endpoint = f"https://api.linkeddata.cultureelerfgoed.nl/queries/rce/Query-11-4/1/run?page={page}&pageSize={page_size}"
headers = {
    "Accept": "application/trig"
}

response = requests.get(sparql_endpoint, headers=headers)

# Controleer of de query succesvol was
if response.status_code == 200:
    # Stap 3: Verwerk de ontvangen RDF data handmatig
    output_lines = []
    rdf_data = response.text.splitlines()

    # Voeg de named graph URI toe aan het begin
    output_lines.append(f"<{new_graph_uri}> {{")

    for line in rdf_data:
        if line.strip() and not line.startswith("@prefix"):
            # Voeg xsd:integer type toe aan het object van de triple
            subject, predicate, object = line.strip().split(' ', 2)
            if object.endswith('.'):
                object = object[:-1].strip()  # Verwijder de laatste punt
            # Voeg "^^<http://www.w3.org/2001/XMLSchema#integer>" toe aan het object
            if object.isdigit():  # Controleer of het object een getal is
                object = f'"{object}"^^<http://www.w3.org/2001/XMLSchema#integer>'
            output_lines.append(f"  {subject} {predicate} {object} .")

    # Sluit de named graph af
    output_lines.append("}")

    # Stap 4: Sla het resultaat op in een TriG-bestand
    output_filename = args.output
    with open(output_filename, "w", encoding="utf-8") as output_file:
        for line in output_lines:
            output_file.write(line + "\n")

    print(f"Graph opgeslagen als {output_filename}")
else:
    print(f"Er is een fout opgetreden: {response.status_code}")
    print(response.text)
