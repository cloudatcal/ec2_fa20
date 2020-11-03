test = {
	"name": "q2",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> tags = boto3.resource('ec2').Instance(instance_id).tags
					>>> tags[0]["Key"]
					'student_name'
					>>> tags[0]["Value"] == tag_value
					True
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