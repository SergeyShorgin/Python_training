{
  "id": "d4cd1153-9624-401e-a307-86baf1647a5f",
  "version": "2.0",
  "name": "gismeteo",
  "url": "https://github.com/",
  "tests": [{
    "id": "0f5bb38c-dab5-4cb8-a38c-5b334e91fb0f",
    "name": "gismo",
    "commands": [{
      "id": "0e2b5385-c20b-4355-9042-6550e405b50a",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "fbf691a0-c73e-4cf4-956d-7d518e2353e1",
      "comment": "",
      "command": "setWindowSize",
      "target": "2121x1400",
      "targets": [],
      "value": ""
    }, {
      "id": "e04a6e13-d2da-4415-91bd-36f86c2afd6d",
      "comment": "",
      "command": "type",
      "target": "id=ya",
      "targets": [
        ["id=ya", "id"],
        ["name=gis20210416123017528", "name"],
        ["css=#ya", "css:finder"],
        ["xpath=//input[@id='ya']", "xpath:attributes"],
        ["xpath=//form[@id='search-city']/div/input", "xpath:idRelative"],
        ["xpath=//form/div/input", "xpath:position"]
      ],
      "value": "москва"
    }, {
      "id": "c427fbc4-d061-4de4-8fd1-4ed65a9775ef",
      "comment": "",
      "command": "sendKeys",
      "target": "id=ya",
      "targets": [
        ["id=ya", "id"],
        ["name=gis20210416123017528", "name"],
        ["css=#ya", "css:finder"],
        ["xpath=//input[@id='ya']", "xpath:attributes"],
        ["xpath=//form[@id='search-city']/div/input", "xpath:idRelative"],
        ["xpath=//form/div/input", "xpath:position"]
      ],
      "value": "${KEY_ENTER}"
    }, {
      "id": "99583e2e-e9b5-41f9-9239-2b280babad60",
      "comment": "",
      "command": "click",
      "target": "css=.districts:nth-child(5) > .group:nth-child(1) li:nth-child(3) b",
      "targets": [
        ["css=.districts:nth-child(5) > .group:nth-child(1) li:nth-child(3) b", "css:finder"],
        ["xpath=//div[@id='citysearch']/div[3]/div[2]/div/div[4]/div/ul/li[3]/a/span/b", "xpath:idRelative"],
        ["xpath=//div[4]/div/ul/li[3]/a/span/b", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "2c8fbe02-81b5-4121-b79d-8addbb38cd40",
      "comment": "",
      "command": "click",
      "target": "css=.weather_more > span",
      "targets": [
        ["css=.weather_more > span", "css:finder"],
        ["xpath=//div[@id='weather-daily']/div[3]/div[5]/div/a/span", "xpath:idRelative"],
        ["xpath=//a/span", "xpath:position"],
        ["xpath=//span[contains(.,'Почасовой прогноз погоды')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "25e97c14-944d-4112-a856-ed836706a629",
    "name": "тест GitHub",
    "commands": [{
      "id": "707a338c-3507-49ba-8a72-9b4d5718cb2f",
      "comment": "",
      "command": "open",
      "target": "https://github.com/",
      "targets": [],
      "value": ""
    }, {
      "id": "b75e00a3-af29-48e4-969f-4ce44edaf768",
      "comment": "",
      "command": "setWindowSize",
      "target": "2121x1400",
      "targets": [],
      "value": ""
    }, {
      "id": "73da66fc-2d7a-408a-9f9c-893bf743417a",
      "comment": "",
      "command": "click",
      "target": "css=.HeaderMenu-link:nth-child(2) > font > font",
      "targets": [
        ["css=.HeaderMenu-link:nth-child(2) > font > font", "css:finder"],
        ["xpath=//div[2]/a/font/font", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "db24cb5c-d12b-467b-acae-83f353c01752",
      "comment": "",
      "command": "type",
      "target": "id=login_field",
      "targets": [
        ["id=login_field", "id"],
        ["name=login", "name"],
        ["css=#login_field", "css:finder"],
        ["xpath=//input[@id='login_field']", "xpath:attributes"],
        ["xpath=//div[@id='login']/div[4]/form/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": "SergeyShorgin"
    }, {
      "id": "cf8956e2-3ff6-4960-be4e-a36d256cc634",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='login']/div[4]/form/div/input", "xpath:idRelative"],
        ["xpath=//form/div/input", "xpath:position"]
      ],
      "value": "Stunt686rider"
    }, {
      "id": "0b3c9a53-72e6-4f77-9474-c05f864a8a13",
      "comment": "",
      "command": "sendKeys",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='login']/div[4]/form/div/input", "xpath:idRelative"],
        ["xpath=//form/div/input", "xpath:position"]
      ],
      "value": "${KEY_ENTER}"
    }, {
      "id": "ecbc238d-1fea-4aea-aff2-27ce52f9380b",
      "comment": "",
      "command": "mouseOver",
      "target": "css=#dashboard-repos-container > #repos-container .flex-shrink-0 > font > font",
      "targets": [
        ["css=#dashboard-repos-container > #repos-container .flex-shrink-0 > font > font", "css:finder"],
        ["xpath=//div[@id='repos-container']/ul/li/div/a/span/font/font", "xpath:idRelative"],
        ["xpath=//div/a/span/font/font", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b09fce97-8c64-41fd-be9e-52bf88af9316",
      "comment": "",
      "command": "click",
      "target": "css=#dashboard-repos-container > #repos-container .flex-shrink-0 > font > font",
      "targets": [
        ["css=#dashboard-repos-container > #repos-container .flex-shrink-0 > font > font", "css:finder"],
        ["xpath=//div[@id='repos-container']/ul/li/div/a/span/font/font", "xpath:idRelative"],
        ["xpath=//div/a/span/font/font", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b62133b5-d0a1-46a3-8701-610f50919e93",
      "comment": "",
      "command": "click",
      "target": "css=.Header-link > .dropdown-caret:nth-child(3)",
      "targets": [
        ["css=.Header-link > .dropdown-caret:nth-child(3)", "css:finder"],
        ["xpath=//summary/span[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "e6e98762-9362-49c5-b45d-849644f6fb1f",
      "comment": "",
      "command": "click",
      "target": "css=.dropdown-signout",
      "targets": [
        ["css=.dropdown-signout", "css:finder"],
        ["xpath=(//button[@type='submit'])[3]", "xpath:attributes"],
        ["xpath=//details-menu/form/button", "xpath:position"],
        ["xpath=//button[contains(.,'выход')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "93cbce43-9b4d-4bd7-9181-1c1467874388",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["0f5bb38c-dab5-4cb8-a38c-5b334e91fb0f"]
  }],
<<<<<<< HEAD
  "urls": ["https://www.gismeteo.ru/", "https://github.com/"],
=======
  "urls": ["https://www.gismeteo.ru/"],
>>>>>>> 6ad829b86db76c09ad80b1b7d01ecb01eeb2ff58
  "plugins": []
}