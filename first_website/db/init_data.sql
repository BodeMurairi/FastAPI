-- Remove all existing rows
DELETE FROM creature;

-- Insert new rows
INSERT INTO creature(name, country, area, description, aka)
VALUES
    ('Loch Ness Monster', 'Scotland', 'Loch Ness', 'A large aquatic creature said to inhabit Loch Ness.', 'Nessie'),
    ('Bigfoot', 'USA', 'Pacific Northwest', 'A large, hairy, ape-like being purported to inhabit forests.', 'Sasquatch'),
    ('Chupacabra', 'Puerto Rico', 'Various regions in the Americas', 'A legendary creature said to attack livestock, especially goats.', 'Goat-sucker'),
    ('Yeti', 'Nepal/Tibet', 'Himalayas', 'An ape-like entity purported to inhabit the Himalayan mountains.', 'Abominable Snowman'),
    ('Mothman', 'USA', 'Point Pleasant, West Virginia', 'A humanoid creature with wings and glowing red eyes.', 'Bode222'),
    ('Jersey Devil', 'USA', 'Pine Barrens, New Jersey', 'A legendary creature said to inhabit the Pine Barrens of southern New Jersey.', 'Bode22'),
    ('Kraken', 'Scandinavia', 'North Atlantic Ocean', 'A legendary sea monster of enormous size said to dwell off the coasts of Norway and Greenland.', 'Bode22'),
    ('Bunyip', 'Australia', 'Australian wetlands and billabongs', 'A mythical creature from Australian Aboriginal mythology, often described as a large water-dwelling animal.', 'Bode22'),
    ('Wendigo', 'Canada/USA', 'Northern forests of the Great Lakes region and Canada', 'A mythical creature or evil spirit from Algonquian folklore, often associated with cannibalism and insatiable greed.', 'Bode22'),
    ('Yetti', 'CN', 'Himalayas', 'Hirsute Himalayan', 'Abominable Snowman');

DELETE FROM explorer;

INSERT INTO explorer(name, country, description)
VALUES
    ('Dr. John Smith', 'USA', 'A renowned cryptozoologist with numerous expeditions to find legendary creatures.'),
    ('Jane Doe', 'UK', 'An adventurous explorer known for her daring quests into uncharted territories.'),
    ('Carlos Ramirez', 'Mexico', 'A folklorist and explorer dedicated to uncovering the truth behind local legends.'),
    ('Akira Tanaka', 'Japan', 'A scientist and explorer with a focus on mysterious phenomena in remote areas.'),
    ('Claude Hande', 'FR', 'Scarce during full moons'),
    ('Léa Dupont', 'FR', 'Expert in folklore and mythical creatures'),
    ('Sophie Martin', 'FR', 'Specializes in cryptid research and expeditions'),
    ('Julien Bernard', 'FR', 'Adventurer and explorer of uncharted territories'),
    ('Isabelle Laurent', 'FR', 'Researcher in ancient myths and legends'),
    ('Antoine Moreau', 'FR', 'Field researcher with a focus on mysterious phenomena'),
    ('Noah Waiser', 'USA', 'Myopic machete man');
