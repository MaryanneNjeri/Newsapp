class Sources:
    '''
    sources class to define the newssources objects
    '''
    def __init__(self,id,name,url,category,country,description):
        self.id=id
        self.name=name
        self.url=url
        self.category=category
        self.country=country
        self.description=description
class Articles:
    '''
    an article class to define the article objects
    '''
    def __init__(self,id,name,author,date,title,url,image,):
        self.id=id
        self.name=name
        self.author=author
        self.date=date
        self.author=author
        self.date=date
        self.title=title
        self.url=url
        self.image=image
