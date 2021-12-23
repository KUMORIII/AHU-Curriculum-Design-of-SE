# Generated by Django 3.2.8 on 2021-12-12 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('cour_id', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='课程代码')),
                ('course_name', models.CharField(max_length=12, verbose_name='课程名')),
                ('classroom', models.CharField(max_length=8, verbose_name='教室')),
                ('week_start', models.IntegerField(default=1, verbose_name='开始周数')),
                ('week_end', models.IntegerField(default=18, verbose_name='结束周数')),
            ],
            options={
                'verbose_name_plural': '课程信息表',
                'db_table': 'course_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('stu_id', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='学号')),
                ('stu_name', models.CharField(max_length=15, verbose_name='姓名')),
                ('sex', models.BooleanField(choices=[(0, '女'), (1, '男')], null=True, verbose_name='性别')),
                ('major', models.CharField(max_length=20, verbose_name='专业')),
                ('stu_passwd', models.CharField(max_length=20, verbose_name='密码')),
            ],
            options={
                'verbose_name': '学生信息表',
                'db_table': 'student_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('tea_id', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='教师编号')),
                ('tea_name', models.CharField(max_length=15, verbose_name='教师名')),
                ('tea_password', models.CharField(max_length=20, verbose_name='密码')),
            ],
            options={
                'verbose_name_plural': '教师信息表',
                'db_table': 'teacher_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TeaCourse',
            fields=[
                ('tea_cour_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('course_id', models.CharField(max_length=7, null=True, verbose_name='课程')),
                ('tea_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login_information.teacherinfo', verbose_name='教师')),
            ],
            options={
                'verbose_name_plural': '教师授课表',
                'db_table': 'tea_course',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ScCourse',
            fields=[
                ('stu_cour_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login_information.courseinfo', verbose_name='课程')),
                ('stu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login_information.studentinfo', verbose_name='学生')),
            ],
            options={
                'verbose_name_plural': '学生选课表',
                'db_table': 'sc_course',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LeaveInfo',
            fields=[
                ('leave_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('weeks', models.IntegerField(verbose_name='周数')),
                ('leave_reason', models.TextField(blank=True, null=True, verbose_name='请假理由')),
                ('leave_state', models.IntegerField(choices=[(0, '待审核'), (1, '未通过'), (2, '通过')], default=0, null=True, verbose_name='申请状态')),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login_information.courseinfo', verbose_name='课程')),
                ('stu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login_information.studentinfo', verbose_name='学生')),
            ],
            options={
                'verbose_name_plural': '请假信息表',
                'db_table': 'leave_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CheckInfo',
            fields=[
                ('check_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('state', models.CharField(choices=[('0', '缺勤'), ('1', '迟到'), ('2', '请假'), ('3', '正常')], default='0', max_length=1, null=True, verbose_name='考勤状态')),
                ('check_week', models.IntegerField(null=True, verbose_name='周数')),
                ('punch_time', models.DateTimeField(blank=True, null=True, verbose_name='打卡时间')),
                ('check_time', models.DateTimeField(blank=True, null=True, verbose_name='正常考勤时间')),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login_information.courseinfo', verbose_name='课程')),
                ('stu_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login_information.studentinfo', verbose_name='学生')),
            ],
            options={
                'verbose_name_plural': '考勤信息表',
                'db_table': 'check_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CheckAppeal',
            fields=[
                ('appeal_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('appeal_reason', models.TextField(blank=True, null=True, verbose_name='请假理由')),
                ('appeal_state', models.IntegerField(choices=[(0, '待审核'), (1, '未通过'), (2, '通过')], default=0, null=True, verbose_name='申诉状态')),
                ('check_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login_information.checkinfo', verbose_name='考勤记录')),
            ],
            options={
                'verbose_name_plural': '考勤申诉表',
                'db_table': 'check_appeal',
                'managed': True,
            },
        ),
    ]
