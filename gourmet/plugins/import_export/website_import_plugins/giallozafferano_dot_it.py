from gourmet.plugin import PluginPlugin
import schema_org_parser
from schema_org_parser import Excluder

class GialloZafferanoPlugin (PluginPlugin):
    target_pluggable = 'webimport_plugin'

    def do_activate (self, pluggable):
        pass
    
    def test_url (self, url, data):
        if 'giallozafferano.it' in url: 
            return 5
        return 0

    def get_importer (self, webpage_importer):
        GialloZafferanoParserBase = schema_org_parser.generate(webpage_importer.WebParser)

        class GialloZafferanoParser(GialloZafferanoParserBase):
            def preparse (self):
                GialloZafferanoParserBase.preparse(self)
                ingredients = self.soup.find(attrs={"class": "ingredienti"}).find('dd')
                self.preparsed_elements.append((iingredients,'ingredients'))
                preptime = self.soup.find(id='preptime').find('strong')
                self.preparsed_elements.append((preptime,'preptime'))
                cooktime = self.soup.find(id='cooktime').find('strong')
                self.preparsed_elements.append((cooktime,'cooktime'))

        return GialloZafferanoParser
