test = {
	"name": "q1",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> recipes_ddb = boto3.resource("dynamodb").Table("recipes")
					>>> recipe = recipes_ddb.get_item(Key={"id": "2e2381f6c21c6bf140"})
					>>> recipe["Item"]["recipe_file"]
					'5b6f2d1865d83c76af.3ds'
					""",
					"hidden": False,
					"locked": False,
				}, 
			],
			"scored": True,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}, 
	]
}