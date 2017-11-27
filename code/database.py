import time



database= {b'Best team in Soccer?':b'Germany.',
           b'Best club team in soccer?':b'Chelsea.',
           b'Best team in Cricket?':b'India.',
           b'Best team in IPL?':b'Mumbai Indians.',
           b'Best team in Basketball?':b'USA.',
           b'Best team in Nba?':b'San Antonio Spurs.',
           b'Number of continents in the world?':b'There are seven continents in the world.',
           b'Biggest continent in the world?':b'Asia is the biggest continent in the world.',
           b'Capital of USA?':b'Washington DC.',
           b'Capital of England?':b'London.',
           b'Target?':b'Store.',
           b'Coscos?':b'Expensive Store.',
           b'Macys?':b'Mall Like Store.',
           b'Wallmart?':b'Cheaper Store.',
           b'Amazon?':b'Online Store.',
           b'Flow of electrons?':b'Electricity.',
           b'Best Car Maker in the World?':b'Lamborghini.',
           b'Time and Tide?':b'Waits for no man.',
           b'Best Civilian Car Maker in the World?':b'Honda.',
           b'Fastest Train in the World?':b'Maglev.',
           b'Fastest Car in the World?':b'Buggatti.',
           b'Biggest Planet in the Solar System?':b'Jupiter.',
           b'Singularity?':b'Black Hole.',
           b'Biggest Known Star in the Universe?':b'VY Canis Majoris.',
           b'Our Galaxy?':b'Milky way.',
           b'Electrical Car Maker?':b'Tesla.',
           b'Go Knights?':b'Charge On.',
           b'Best Band in the World?':b'Linkin Park.',
           b'Video Streaming Website?':b'Youtube.',
           b'May the Force be with you?':b'Star Wars.'}#The entire dictionary dataset
        
            


def fetch_reply(answer):
    time.sleep(3)
    return database.get(answer,b'Error: Unknown Information.')#Will throw the error if data is not found in the data set
