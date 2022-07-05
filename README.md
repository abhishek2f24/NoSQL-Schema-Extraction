<h3>Extract schema from JSON, XML and TXT file</h3>

<h1>JSON</h1>
Relational databases such as MySQL, Oracle, PostgreSQL can be queried and extract using SQL whereas NoSQL databases, most have native support for JSON as an import format. This means you can export data in JSON format from one NoSQL database like Mongo, Cassandra, Neo4j, OrientDB and import the same data to another NoSQL database like RethinkDB, CouchDB, DocumentDB and RethinkDB  without doing any conversion. In this repo we have created some scripts to extract levelwise schema from <a href="https://github.com/abhishek2f24/NoSQL-Schema-Extraction/tree/main/JSON">JSON</a>.

```
#sample json structure
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

```

Extracted Schema will be 
```
['glossary']                                                #for level 1
['glossary.title', 'glossary.GlossDiv']                     #for level 2
['glossary.title', 'GlossDiv.title', 'GlossDiv.GlossList']  #for level 3
#and same goes on
```


<h1>XML</h1>
XML is another format we can use to get data from NoSQL although its less common. The famous XML databases are Oracle database, MarkLogic exist and MarkLogic Cassandra. Either we convert XML to JSON using ```XMLtoDict``` and then use above scripts to extract schema (which is not recommended because an XML file may be of few GB in size, and it takes a hell of time to convert) or we can extract levelwise schema using scripts<a href="https://github.com/abhishek2f24/NoSQL-Schema-Extraction/tree/main/XML">here</a>.
.

```
#sample XML structure
<note>
    <to id='title'>Tove</to>
        <from>Jani</from>
           <heading class='red'>Reminder</heading>
                <body>Don't forget me this weekend!</body>
</note>
```
Extracted Schema will be
```
note
note/to
note/to/@title      #attributes will be displayed followed by @
note/to/from
note/to/from/heading
note/to/from/heading/body
```
<h1>TXT</h1>
Advantage stores data for Xbase memo fields in DBT and FPT memo file formats depending on which Advantage database driver was used to open the corresponding table. When using the Advantage NTX driver, DBT memo files are supported. For FPT memos, the Advantage CDX driver must be used.These .dbt, .dbf, .fpt formats which can be seen with notepad++, either copy the content of the file into a txt file or figure out how python can read the file format. Once file content is loaded into python, use custom scripts to extract data from <a href="https://github.com/abhishek2f24/NoSQL-Schema-Extraction/tree/main/TXT">here</a>.
. 

```
#sample .dbt, .dbf file content saved as .txt file
Table cost
ID source datatime fieldname
#some random data
Table Bill
ID department quantity
#some random data
```

Extracted Schema will be
```
['cost.ID', 'cost.source', 'cost.datetime', 'cost.fieldname', 'Bill.ID', 'Bill.department', 'Bill.quantity']
```
