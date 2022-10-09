Copy-Item "./lambda_function.py" -Destination "./lambda"

Compress-Archive -Path ./lambda/* -DestinationPath ./lambda.zip

Remove-Item ./lambda/lambda_function.py
