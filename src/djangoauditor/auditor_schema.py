# Auditor schema builder
from django_auditor_logs.auditor_schema.builder import AuditorSchemaBuilder

# build the Auditor schema
auditor_schema = AuditorSchemaBuilder()
auditor_query=auditor_schema.build_auditor_schema()

# Build the schema
import graphene

class Query(auditor_query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)


