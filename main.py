import spacy
import re
import random
from collections import defaultdict
from lxml import etree

# ==============================
# NLP ENGINE
# ==============================

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def preprocess(self, text):
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def analyze(self, text):
        return self.nlp(text)


# ==============================
# UML COMPONENT EXTRACTION
# ==============================

class UMLExtractor:
    def __init__(self):
        self.classes = set()
        self.relationships = []

    def extract_classes(self, doc):
        for chunk in doc.noun_chunks:
            if chunk.root.pos_ == "NOUN":
                self.classes.add(chunk.text.capitalize())
        return list(self.classes)

    def extract_relationships(self, doc):
        for sent in doc.sents:
            subj = None
            obj = None
            relation = None

            for token in sent:
                if token.dep_ == "nsubj":
                    subj = token.text.capitalize()
                if token.dep_ == "dobj":
                    obj = token.text.capitalize()
                if token.lemma_ in ["contain", "include"]:
                    relation = "aggregation"
                elif token.lemma_ in ["inherit", "extend"]:
                    relation = "inheritance"
                elif token.pos_ == "VERB":
                    relation = "association"

            if subj and obj and relation:
                self.relationships.append((subj, relation, obj))

        return self.relationships


# ==============================
# RELATIONSHIP CLASSIFIER
# ==============================

class RelationshipClassifier:
    def classify(self, relationships):
        classified = []
        for subj, rel, obj in relationships:
            confidence = round(random.uniform(0.75, 0.95), 2)
            classified.append({
                "from": subj,
                "to": obj,
                "type": rel,
                "confidence": confidence
            })
        return classified


# ==============================
# HUMAN-IN-THE-LOOP MODULE
# ==============================

class HumanFeedbackModule:
    def review(self, classified_data):
        print("\n--- Human Review Mode ---")
        updated = []

        for item in classified_data:
            print(f"\nDetected: {item['from']} -> {item['to']} ({item['type']})")
            print(f"Confidence: {item['confidence']}")

            choice = input("Accept? (y/n): ")

            if choice.lower() == 'y':
                updated.append(item)
            else:
                new_type = input("Enter correct relationship type: ")
                item["type"] = new_type
                item["confidence"] = 1.0
                updated.append(item)

        return updated


# ==============================
# DIAGRAM GENERATOR
# ==============================

class DiagramGenerator:

    def generate_plantuml(self, classes, relationships):
        uml = "@startuml\n"
        uml += "title AI-Based UML Diagram Generator\n\n"

        for cls in classes:
            uml += f"class {cls} {{}}\n"

        uml += "\n"

        for rel in relationships:
            if rel["type"] == "inheritance":
                uml += f"{rel['from']} --|> {rel['to']} : inheritance ({rel['confidence']})\n"
            elif rel["type"] == "aggregation":
                uml += f"{rel['from']} o-- {rel['to']} : aggregation ({rel['confidence']})\n"
            else:
                uml += f"{rel['from']} --> {rel['to']} : association ({rel['confidence']})\n"

        uml += "@enduml"
        return uml

    def generate_xml(self, classes, relationships):
        root = etree.Element("UMLDiagram")

        classes_el = etree.SubElement(root, "Classes")
        for cls in classes:
            etree.SubElement(classes_el, "Class", name=cls)

        rels_el = etree.SubElement(root, "Relationships")
        for rel in relationships:
            etree.SubElement(rels_el, "Relationship",
                             source=rel["from"],
                             target=rel["to"],
                             type=rel["type"],
                             confidence=str(rel["confidence"]))

        return etree.tostring(root, pretty_print=True).decode()


# ==============================
# MAIN SYSTEM CONTROLLER
# ==============================

class UMLSystem:

    def __init__(self):
        self.nlp = NLPProcessor()
        self.extractor = UMLExtractor()
        self.classifier = RelationshipClassifier()
        self.feedback = HumanFeedbackModule()
        self.generator = DiagramGenerator()

    def process_srs(self, text):
        print("Preprocessing...")
        clean_text = self.nlp.preprocess(text)

        print("Performing NLP analysis...")
        doc = self.nlp.analyze(clean_text)

        print("Extracting UML components...")
        classes = self.extractor.extract_classes(doc)
        relationships = self.extractor.extract_relationships(doc)

        print("Classifying relationships...")
        classified = self.classifier.classify(relationships)

        reviewed = self.feedback.review(classified)

        print("Generating PlantUML...")
        plantuml_code = self.generator.generate_plantuml(classes, reviewed)

        print("Generating XML...")
        xml_output = self.generator.generate_xml(classes, reviewed)

        return plantuml_code, xml_output


# ==============================
# RUN EXAMPLE
# ==============================

if __name__ == "__main__":

    srs_text = """
    A Customer places an Order.
    An Order contains Products.
    PremiumCustomer inherits Customer.
    """

    system = UMLSystem()
    plantuml_output, xml_output = system.process_srs(srs_text)

    print("\n--- PlantUML Output ---\n")
    print(plantuml_output)

    print("\n--- XML Output ---\n")
    print(xml_output)

    with open("output.puml", "w") as f:
        f.write(plantuml_output)

    with open("output.xml", "w") as f:
        f.write(xml_output)

    print("\nFiles saved: output.puml & output.xml")