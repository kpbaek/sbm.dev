# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Product.status'
        db.delete_column(u'plts_product', 'status_id')

        # Adding field 'Product.product_status'
        db.add_column(u'plts_product', 'product_status',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['plts.ProductStatus']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Product.status'
        db.add_column(u'plts_product', 'status',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['plts.ProductStatus']),
                      keep_default=False)

        # Deleting field 'Product.product_status'
        db.delete_column(u'plts_product', 'product_status_id')


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
            'product_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plts.ProductStatus']"}),
            'reg_date': ('django.db.models.fields.DateTimeField', [], {})
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