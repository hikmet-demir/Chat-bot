class cleaner:
    number = ""
    def __init__(self,number,files):
        self.number = number
        self.files = files
        self.messages = ""
        self.people = ""
        self.input_lines = ""

    def open_files(self):
        for file_name in self.files:
            with open(file_name,'r',encoding= "utf-8") as f:
                self.read_data = f.read()
                self.file_process()
            
    def file_process(self):
        self.input_lines = self.read_data.splitlines()

        merge_lines = []
        for j in self.input_lines:
            if '/' in j[0:10] and ',' in j[0:10]:
                merge_lines.append(j)
            else:
                merge_lines[-1] = merge_lines[-1] + " " + j

        self.input_lines = merge_lines

        self.people = []
        self.messages = []
        for i in (self.input_lines):
            try:
                splitted = i.split(':')

                self.people.append(splitted[1][splitted[1].find('-')+2:].replace(" ",""))

                if len(splitted) > 2:
                    self.messages.append(splitted[2][1:])
                else:
                    self.messages.append("")

            except:
                print("FILE_PROCESS ERROR")

        self.person()
        print(self.people)

    def person(self):
        counter = 0
        for message,person in zip(self.messages,self.people):
            if self.number in person:
                counter += 1
        print(counter)
            
        


ekin = cleaner("+905075828463",["WhatsApp Chat with Bölüm EE 2017.txt"
                                    ,"WhatsApp Chat with EE 2016.txt",
                                    "WhatsApp Chat with IEEE Bilkent Aktif.txt"])
ekin.open_files()