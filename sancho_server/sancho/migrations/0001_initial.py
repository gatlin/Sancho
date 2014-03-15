# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContentType'
        db.create_table(u'sancho_contenttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=10000)),
        ))
        db.send_create_signal(u'sancho', ['ContentType'])

        # Adding model 'LinkType'
        db.create_table(u'sancho_linktype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=10000)),
        ))
        db.send_create_signal(u'sancho', ['LinkType'])

        # Adding model 'Post'
        db.create_table(u'sancho_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['sancho.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('content', self.gf('json_field.fields.JSONField')(default=u'null')),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'sancho', ['Post'])

        # Adding model 'Link'
        db.create_table(u'sancho_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='links', to=orm['sancho.Post'])),
            ('to_post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sancho.Post'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sancho.LinkType'])),
        ))
        db.send_create_signal(u'sancho', ['Link'])


    def backwards(self, orm):
        # Deleting model 'ContentType'
        db.delete_table(u'sancho_contenttype')

        # Deleting model 'LinkType'
        db.delete_table(u'sancho_linktype')

        # Deleting model 'Post'
        db.delete_table(u'sancho_post')

        # Deleting model 'Link'
        db.delete_table(u'sancho_link')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sancho.contenttype': {
            'Meta': {'object_name': 'ContentType'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'sancho.link': {
            'Meta': {'object_name': 'Link'},
            'from_post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': u"orm['sancho.Post']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sancho.Post']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sancho.LinkType']"})
        },
        u'sancho.linktype': {
            'Meta': {'object_name': 'LinkType'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'sancho.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('json_field.fields.JSONField', [], {'default': "u'null'"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['sancho.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'uid': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sancho']