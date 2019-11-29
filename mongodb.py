from dotenv import load_dotenv


load_dotenv()

#Environment variable: 
connectionURL = os.getenv("MONGODB_URL")

class CollConection:

    def __init__(self,connectionurl, dbName,collection):
        self.client = MongoClient(connectionURL)
        self.db = self.client[dbName]
        self.collection=self.db[collection]

    def addDocument(self,document):
        a=self.collection.insert_one(document)
        print("Inserted", a.inserted_id)
        return a.inserted_id
    
    def addChiste(self, autor, chiste):
        document={'autor':autor,
                'chiste':chiste}
        return self.addDocument(document)

coll = CollConnection(connectionURL)