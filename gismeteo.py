{
  "id": "d4cd1153-9624-401e-a307-86baf1647a5f",
  "version": "2.0",
  "name": "gismeteo",
  "url": "https://www.gismeteo.ru",
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
  }],
  "suites": [{
    "id": "93cbce43-9b4d-4bd7-9181-1c1467874388",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["0f5bb38c-dab5-4cb8-a38c-5b334e91fb0f"]
  }],
  "urls": ["https://www.gismeteo.ru/"],
  "plugins": []
}