# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductStatus'
        db.create_table(u'plts_productstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'plts', ['ProductStatus'])

        # Adding model 'RepairErrorType'
        db.create_table(u'plts_repairerrortype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'plts', ['RepairErrorType'])

        # Adding model 'Part'
        db.create_table(u'plts_part', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.PartType'])),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('reg_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'plts', ['Part'])

        # Adding model 'Company'
        db.create_table(u'plts_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'plts', ['Company'])

        # Adding model 'PartType'
        db.create_table(u'plts_parttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.ProductModel'])),
            ('part_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.PartClass'])),
            ('version', self.gf('django.db.models.fields.IntegerField')()),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.Company'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('reg_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'plts', ['PartType'])

        # Adding model 'ManufacturingHistory'
        db.create_table(u'plts_manufacturinghistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manufacturing_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.ManufacturingType'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.Product'])),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.Part'])),
            ('repair_error_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.RepairErrorType'])),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('worker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.Worker'])),
            ('reg_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'plts', ['ManufacturingHistory'])

        # Adding model 'ProductModel'
        db.create_table(u'plts_productmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('barcode_prefix', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'plts', ['ProductModel'])

        # Adding model 'Worker'
        db.create_table(u'plts_worker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.Company'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'plts', ['Worker'])

        # Adding model 'Product'
        db.create_table(u'plts_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.ProductModel'])),
            ('barcode', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plts.ProductStatus'])),
            ('reg_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'plts', ['Product'])

        # Adding model 'ManufacturingType'
        db.create_table(u'plts_manufacturingtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'plts', ['ManufacturingType'])

        # Adding model 'PartClass'
        db.create_table(u'plts_partclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'plts', ['PartClass'])


    def backwards(self, orm):
        # Deleting model 'ProductStatus'
        db.delete_table(u'plts_productstatus')

        # Deleting model 'RepairErrorType'
        db.delete_table(u'plts_repairerrortype')

        # Deleting model 'Part'
        db.delete_table(u'plts_part')

        # Deleting model 'Company'
        db.delete_table(u'plts_company')

        # Deleting model 'PartType'
        db.delete_table(u'plts_parttype')

        # Deleting model 'ManufacturingHistory'
        db.delete_table(u'plts_manufacturinghistory')

        # Deleting model 'ProductModel'
        db.delete_table(u'plts_productmodel')

        # Deleting model 'Worker'
        db.delete_table(u'plts_worker')

        # Deleting model 'Product'
        db.delete_table(u'plts_product')

        # Deleting model 'ManufacturingType'
        db.delete_table(u'plts_manufacturingtype')

        # Deleting model 'PartClass'
        db.delete_table(u'plts_partclass')


    models = {
        u'plts.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'plts.manufacturinghistory': {
            'Meta': {'object_name': 'ManufacturingHistory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturing_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.ManufacturingType']"}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.Part']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.Product']"}),
            'reg_date': ('django.db.models.fields.DateTimeField', [], {}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'repair_error_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.RepairErrorType']"}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.Worker']"})
        },
        u'plts.manufacturingtype': {
            'Meta': {'object_name': 'ManufacturingType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'plts.part': {
            'Meta': {'object_name': 'Part'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'part_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.PartType']"}),
            'reg_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'plts.partclass': {
            'Meta': {'object_name': 'PartClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'plts.parttype': {
            'Meta': {'object_name': 'PartType'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part_class': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.PartClass']"}),
            'product_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.ProductModel']"}),
            'reg_date': ('django.db.models.fields.DateTimeField', [], {}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        },
        u'plts.product': {
            'Meta': {'object_name': 'Product'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.ProductModel']"}),
            'reg_date': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.ProductStatus']"})
        },
        u'plts.productmodel': {
            'Meta': {'object_name': 'ProductModel'},
            'barcode_prefix': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'plts.productstatus': {
            'Meta': {'object_name': 'ProductStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'plts.repairerrortype': {
            'Meta': {'object_name': 'RepairErrorType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'plts.worker': {
            'Meta': {'object_name': 'Worker'},
            'barcode': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['plts']