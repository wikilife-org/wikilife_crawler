# coding=utf-8

class TestUtils(object):
    
    @staticmethod
    def get_profile_tpl():
        return {
        "update_time" : None,
        "fields" : {
            "status" : 1,
            "items" : [
                {
                    "weight" : "",
                    "title" : "Weight",
                    "node_namespace" : "wikilife.profile.body.weight.value-node",
                    "value" : "",
                    "properties" : {
                        "log" : True,
                        "default" : "70.0",
                        "max_value" : "250.0",
                        "min_value" : "1.0",
                        "value_unit" : "kg",
                        "value_type" : "range",
                        "range_step" : "0.1"
                    },
                    "node_id" : 1140,
                    "slug" : "weight"
                },
                {
                    "properties" : {
                        "log" : True,
                        "default" : "1.70",
                        "max_value" : "2.50",
                        "min_value" : "0.01",
                        "value_unit" : "m",
                        "value_type" : "range",
                        "range_step" : "0.01"
                    },
                    "title" : "Height",
                    "node_namespace" : "wikilife.profile.body.height.value-node",
                    "value" : "",
                    "height" : "",
                    "node_id" : 1142,
                    "slug" : "height"
                },
                {
                    "title" : "Eye Color",
                    "node_namespace" : "wikilife.profile.body.eyes.eye-color.value-node",
                    "eye-color" : "",
                    "value" : "",
                    "properties" : {
                        "default" : "Brown",
                        "value_type" : "text",
                        "options" : [
                            "Black",
                            "Amber",
                            "Blue",
                            "Brown",
                            "Gray",
                            "Green",
                            "Hazel",
                            "Red"
                        ],
                        "log" : True
                    },
                    "node_id" : 1145,
                    "slug" : "eye-color"
                },
                {
                    "title" : "Skin Color",
                    "node_namespace" : "wikilife.profile.body.skin-color.value-node",
                    "value" : "",
                    "properties" : {
                        "default" : "Light Intermediate",
                        "value_type" : "text",
                        "options" : [
                            "Very Light",
                            "Light",
                            "Light Intermediate",
                            "Dark Intermediate",
                            "Dark",
                            "Very Dark"
                        ],
                        "log" : True
                    },
                    "node_id" : 1147,
                    "skin-color" : "",
                    "slug" : "skin-color"
                },
                {
                    "title" : "Hair Amount",
                    "node_namespace" : "wikilife.profile.body.hair.hair-amount.value-node",
                    "value" : "",
                    "properties" : {
                        "default" : "Intermediate",
                        "value_type" : "text",
                        "options" : [
                            "Abundant",
                            "Intermediate",
                            "Too Little",
                            "Bald"
                        ],
                        "log" : True
                    },
                    "node_id" : 1150,
                    "hair-amount" : "",
                    "slug" : "hair-amount"
                },
                {
                    "title" : "Hair Color",
                    "node_namespace" : "wikilife.profile.body.hair.hair-color.value-node",
                    "hair-color" : "",
                    "value" : "",
                    "properties" : {
                        "default" : "Brown",
                        "value_type" : "text",
                        "options" : [
                            "Black",
                            "Brown",
                            "Auburn",
                            "Chestnut",
                            "Red",
                            "Blond",
                            "Gray",
                            "White"
                        ],
                        "log" : True
                    },
                    "node_id" : 1152,
                    "slug" : "hair-color"
                },
                {
                    "properties" : {
                        "default" : "Single",
                        "log" : True,
                        "value_type" : "text",
                        "options" : [
                            "Single",
                            "Married",
                            "Boyfriend",
                            "Girlfriend",
                            "Lover"
                        ]
                    },
                    "title" : "Life Partners",
                    "node_namespace" : "wikilife.profile.personal-info.marital-status.value-node",
                    "value" : "",
                    "slug" : "marital-status",
                    "node_id" : 1155,
                    "marital-status" : ""
                },
                {
                    "title" : "Birthdate",
                    "node_namespace" : "wikilife.profile.personal-info.birthdate.value-node",
                    "birthdate" : "",
                    "properties" : {
                        "value_type" : "datetime",
                        "log" : True,
                    },
                    "node_id" : 1157,
                    "value" : "",
                    "slug" : "birthdate"
                },
                {
                    "title" : "Gender",
                    "gender" : "",
                    "node_namespace" : "wikilife.profile.personal-info.gender.value-node",
                    "value" : "",
                    "properties" : {
                        "default" : "Male",
                        "value_type" : "text",
                        "options" : [
                            "Male",
                            "Female"
                        ],
                        "log" : True
                    },
                    "node_id" : 1159,
                    "slug" : "gender"
                },
                {
                    "title" : "Country",
                    "country" : "",
                    "node_namespace" : "wikilife.profile.personal-info.location.country.value-node",
                    "value" : "",
                    "properties" : {
                        "value_type" : "text",
                        "log" : True,
                    },
                    "node_id" : 1162,
                    "slug" : "country"
                },
                {
                    "properties" : {
                        "value_type" : "text",
                        "log" : True,
                    },
                    "title" : "Region",
                    "region" : "",
                    "value" : "",
                    "slug" : "region",
                    "node_id" : 1164,
                    "node_namespace" : "wikilife.profile.personal-info.location.region.value-node"
                },
                {
                    "city" : "",
                    "title" : "City",
                    "node_namespace" : "wikilife.profile.personal-info.location.city.value-node",
                    "value" : "",
                    "properties" : {
                        "value_type" : "text",
                        "log" : True,
                    },
                    "node_id" : 1166,
                    "slug" : "city"
                },
                {
                    "title" : "Ethnicity",
                    "node_namespace" : "wikilife.profile.personal-info.ethnicity.value-node",
                    "value" : "",
                    "properties" : {
                        "default" : "Caucasian-hispanic",
                        "log" : True,
                        "value_type" : "text",
                        "options" : [
                            "Caucasian-hispanic",
                            "Caucasian-nonhispanic",
                            "African American",
                            "Asian",
                            "American Indian/Alaskan Native",
                            "Native Hawaiian"
                        ]
                    },
                    "node_id" : 1170,
                    "slug" : "ethnicity",
                    "ethnicity" : ""
                },
                {
                    "people" : "",
                    "node_namespace" : "wikilife.profile.personal-info.living-with.people.value-node",
                    "title" : "People",
                    "value" : "",
                    "properties" : {
                        "log" : False,
                        "default" : "Parents",
                        "value_type" : "text",
                        "property" : False,
                        "options" : [
                            "Parents",
                            "Partner",
                            "Roommate",
                            "Partner and kids",
                            "Friends",
                            "Alone",
                            "Grandparents",
                            "Other relatives"
                        ]
                    },
                    "node_id" : 241460,
                    "slug" : "people"
                },
                {
                    "title" : "Pets",
                    "node_namespace" : "wikilife.profile.personal-info.living-with.pets.value-node",
                    "value" : "",
                    "properties" : {
                        "log" : False,
                        "default" : "None",
                        "value_type" : "text",
                        "property" : False,
                        "options" : [
                            "None",
                            "Dog",
                            "Cat",
                            "Turtle",
                            "Hamster",
                            "Rabbit",
                            "Birds",
                            "Other"
                        ]
                    },
                    "node_id" : 241476,
                    "pets" : "",
                    "slug" : "pets"
                }
            ],
            "user_id" : None,
            "avatar" : None
        },
        "model" : "Profile",
        "create_time" : None,
        "server_id" : None
    }
