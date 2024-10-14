{{ define "conductor.name" }}
## default in below statement is used to return first non-empty value from right to left
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{ end }}

{{ define "conductor.fullName" }}
{{- default .Chart.Name .Values.fullNameOverride | trunc 63 | trimSuffix "-" -}}
{{ end }}