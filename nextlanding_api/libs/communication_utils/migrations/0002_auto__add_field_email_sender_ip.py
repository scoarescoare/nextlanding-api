# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Email.sender_ip'
        db.add_column(u'communication_utils_email', 'sender_ip',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Email.sender_ip'
        db.delete_column(u'communication_utils_email', 'sender_ip')


    models = {
        u'communication_utils.email': {
            'Meta': {'unique_together': "(('message_id', 'sent_date'),)", 'object_name': 'Email'},
            'SPF': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'cc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'charsets': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dkim': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'email_direction': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'}),
            'envelope': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.TextField', [], {}),
            'headers': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_reply_to_message_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sender_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'spam_report': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'spam_score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'to': ('django.db.models.fields.TextField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['communication_utils']