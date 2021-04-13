{
  "id": "e3d51e2c-8808-4742-bcc2-8cca2fb88a40",
  "version": "2.0",
  "name": "1",
  "url": "https://tv.yandex.ru",
  "tests": [{
    "id": "463b93c7-0ca8-43e2-a3c0-2ec4c8adac35",
    "name": "матч тв",
    "commands": [{
      "id": "d7b2a7e9-a448-4048-8d84-6818448bdbe8",
      "comment": "",
      "command": "open",
      "target": "/213?period=now&grid=main",
      "targets": [],
      "value": ""
    }, {
      "id": "5e186dfb-583d-4e1e-a179-470c4528eb5c",
      "comment": "",
      "command": "setWindowSize",
      "target": "2121x1400",
      "targets": [],
      "value": ""
    }, {
      "id": "ef9ee161-5fc1-4d9c-bfd1-a969756ec736",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.button_channel-genres",
      "targets": [
        ["css=.button_channel-genres", "css:finder"],
        ["xpath=//button[@type='button']", "xpath:attributes"],
        ["xpath=//div[@id='mount']/div/main/div/div/div[2]/div/div/div/button", "xpath:idRelative"],
        ["xpath=//div/div/button", "xpath:position"],
        ["xpath=//button[contains(.,'Основные')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "f8ce4ecd-7819-449c-9295-9acbe2090929",
      "comment": "",
      "command": "mouseOut",
      "target": "css=.button_channel-genres",
      "targets": [
        ["css=.button_channel-genres", "css:finder"],
        ["xpath=//button[@type='button']", "xpath:attributes"],
        ["xpath=//div[@id='mount']/div/main/div/div/div[2]/div/div/div/button", "xpath:idRelative"],
        ["xpath=//div/div/button", "xpath:position"],
        ["xpath=//button[contains(.,'Основные')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "2b7cfc1a-e2c5-48d1-8455-fd7138667145",
      "comment": "",
      "command": "click",
      "target": "name=text",
      "targets": [
        ["name=text", "name"],
        ["css=.input__control", "css:finder"],
        ["xpath=//input[@name='text']", "xpath:attributes"],
        ["xpath=//div[@id='mount']/div/header/div[2]/div/div/form/div/div/span/span/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "c94488ac-9061-4470-917d-d78f4a6aa13d",
      "comment": "",
      "command": "type",
      "target": "name=text",
      "targets": [
        ["name=text", "name"],
        ["css=.input__control", "css:finder"],
        ["xpath=//input[@name='text']", "xpath:attributes"],
        ["xpath=//div[@id='mount']/div/header/div[2]/div/div/form/div/div/span/span/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "матч тв"
    }, {
      "id": "8a5937ae-11a8-4499-9441-b49eb1d5a209",
      "comment": "",
      "command": "sendKeys",
      "target": "name=text",
      "targets": [
        ["name=text", "name"],
        ["css=.input__control", "css:finder"],
        ["xpath=//input[@name='text']", "xpath:attributes"],
        ["xpath=//div[@id='mount']/div/header/div[2]/div/div/form/div/div/span/span/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "${KEY_ENTER}"
    }, {
      "id": "8b099d80-f42a-4cda-a329-1c899fdf48c7",
      "comment": "",
      "command": "click",
      "target": "css=.link_hovered > .channel-snippet__title",
      "targets": [
        ["css=.link_hovered > .channel-snippet__title", "css:finder"],
        ["xpath=//div[@id='mount']/div/main/div[2]/div/div[2]/div[4]/a/h2", "xpath:idRelative"],
        ["xpath=//div[4]/a/h2", "xpath:position"],
        ["xpath=//h2[contains(.,'Матч Премьер')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "28093242-4213-4350-bb17-192757d6271c",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.button_theme_grey",
      "targets": [
        ["css=.button_theme_grey", "css:finder"],
        ["xpath=//button[@type='button']", "xpath:attributes"],
        ["xpath=//div[@id='mount']/div/main/div/div/div/div/div[2]/div/button", "xpath:idRelative"],
        ["xpath=//div[2]/div/button", "xpath:position"],
        ["xpath=//button[contains(.,'В избранные')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "142c10c2-7d82-4631-98a2-746a831c4d24",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["463b93c7-0ca8-43e2-a3c0-2ec4c8adac35"]
  }],
  "urls": ["https://tv.yandex.ru/"],
  "plugins": []
}