from playwright.sync_api import Page, expect

# Tests for your routes go here
'''
We can get formatted albums with release year
from the /albums page
'''
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f'http://{test_web_address}/albums')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Title: Doolittle \nReleased: 1989',
        'Title: Surfer Rosa \nReleased: 1988'
    ])

def test_get_specific_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f'http://{test_web_address}/albums')
    page.click('text=Doolittle')
    title_element = page.locator('.t-title')
    expect(title_element).to_have_text([
        'Doolittle'
    ])

'''
When we click on 'see artists list' on /albums page
we get a formatted list of artists from
the /artists page
'''

def test_list_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f'http://{test_web_address}/artists')
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Pixies',
        'ABBA',
        'Taylor Swift',
        'Nina Simone'
    ])
    

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page: Page, test_web_address: str): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===
